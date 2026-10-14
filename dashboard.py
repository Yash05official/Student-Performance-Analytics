
"""Interactive Student Performance Analytics Dashboard."""

import pandas as pd
import plotly.express as px
import streamlit as st

from main import load_data

from functions import (
    SUBJECTS,
    validate_data,
    analyze_data,
    summary_statistics,
    subject_averages,
)

st.set_page_config(
    page_title="Student Performance Analytics",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Student Performance Analytics")
st.caption(
    "Analyze student marks, grades, attendance "
    "and department performance."
)

# Sidebar: optional CSV upload
with st.sidebar:
    st.header("Dashboard Filters")

    uploaded_file = st.file_uploader(
        "Upload a CSV dataset (optional)",
        type=["csv"],
    )

    st.caption(
        "Required columns: Student_ID, Name, Department, "
        "Python, Mathematics, AI, Attendance"
    )

# Load data safely
try:
    if uploaded_file is not None:
        raw_df = pd.read_csv(uploaded_file)
    else:
        raw_df = load_data()

    issues = validate_data(raw_df)
    df = analyze_data(raw_df)

except Exception as error:
    st.error(f"Unable to load the dataset: {error}")
    st.stop()

# Display validation messages
if issues:
    with st.expander(
        f"Data quality warnings ({len(issues)})",
        expanded=True,
    ):
        for issue in issues:
            st.warning(issue)
else:
    st.success(
        "Data validation passed. No common data-quality "
        "issues were detected."
    )

# Filters
with st.sidebar:
    departments = sorted(
        df["Department"].dropna().unique().tolist()
    )

    selected_departments = st.multiselect(
        "Department",
        departments,
        default=departments,
    )

    result_options = ["Pass", "Fail", "Incomplete"]

    selected_results = st.multiselect(
        "Student result",
        result_options,
        default=result_options,
    )

filtered = df[
    df["Department"].isin(selected_departments)
    & df["Result"].isin(selected_results)
].copy()

if filtered.empty:
    st.info(
        "No students match these filters. "
        "Change the selections in the sidebar."
    )
    st.stop()

# Summary cards
stats = summary_statistics(filtered)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total students",
    stats["total_students"],
)

col2.metric(
    "Class average",
    f'{stats["class_average"]:.2f}/100',
)

col3.metric(
    "Pass percentage",
    f'{stats["pass_percentage"]:.1f}%',
)

col4.metric(
    "Average attendance",
    f'{stats["average_attendance"]:.1f}%',
)

st.divider()

# Charts: subject averages and grade distribution
left, right = st.columns(2)

with left:
    st.subheader("Subject-wise averages")

    subject_df = subject_averages(filtered)

    fig = px.bar(
        subject_df,
        x="Subject",
        y="Average Marks",
        color="Subject",
        text="Average Marks",
        range_y=[0, 100],
        title="Average marks by subject",
    )

    fig.update_traces(
        texttemplate="%{text:.1f}",
        textposition="outside",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

with right:
    st.subheader("Grade distribution")

    grade_order = ["A+", "A", "B", "C", "D", "F", "N/A"]

    grade_counts = (
        filtered["Grade"]
        .value_counts()
        .reindex(grade_order, fill_value=0)
    )

    grade_df = (
        grade_counts[grade_counts > 0]
        .rename_axis("Grade")
        .reset_index(name="Students")
    )

    fig = px.pie(
        grade_df,
        names="Grade",
        values="Students",
        hole=0.45,
        title="Students by grade",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

# Charts: department and attendance
left, right = st.columns(2)

with left:
    st.subheader("Department performance")

    department_df = (
        filtered.groupby("Department", as_index=False)
        ["Average"]
        .mean()
        .round(2)
    )

    fig = px.bar(
        department_df,
        x="Department",
        y="Average",
        text="Average",
        range_y=[0, 100],
        title="Average marks by department",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

with right:
    st.subheader("Attendance vs marks")

    fig = px.scatter(
        filtered,
        x="Attendance",
        y="Average",
        color="Department",
        hover_name="Name",
        hover_data=["Grade", "Result"],
        range_x=[0, 100],
        range_y=[0, 100],
        title="Attendance compared with average marks",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

st.divider()

# Search and display student records
st.subheader("Student records")

search = st.text_input(
    "Search by student name or ID"
)

table = filtered.copy()

if search.strip():
    query = search.strip().lower()

    matches_name = (
        table["Name"]
        .astype(str)
        .str.lower()
        .str.contains(query, na=False)
    )

    matches_id = (
        table["Student_ID"]
        .astype(str)
        .str.contains(query, na=False)
    )

    table = table[matches_name | matches_id]

display_columns = [
    "Student_ID",
    "Name",
    "Department",
    *SUBJECTS,
    "Total",
    "Average",
    "Grade",
    "Result",
    "Attendance",
]

st.dataframe(
    table[display_columns].sort_values(
        "Average", ascending=False
    ),
    use_container_width=True,
    hide_index=True,
)

# Download the filtered report
csv_data = table[display_columns].to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="⬇️ Download filtered report (CSV)",
    data=csv_data,
    file_name="student_performance_report.csv",
    mime="text/csv",
)

st.caption(
    "Passing requires at least 40 marks in every subject. "
    "Attendance is analyzed separately."
)
