import streamlit as st

from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills
from job_matcher import compare_skills, calculate_similarity
from ats_analyzer import analyze_ats
from recommendations import generate_recommendations


# ---------------------------------
# Page Configuration
# ---------------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# ---------------------------------
# Header
# ---------------------------------

st.title("📄 AI Resume Analyzer")

st.write(
    "Analyze your resume against a job description "
    "using skill matching, text similarity, and ATS checks."
)

st.divider()


# ---------------------------------
# Input Section
# ---------------------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("📤 Upload Resume")

    resume_file = st.file_uploader(
        "Upload your resume in PDF format",
        type=["pdf"]
    )


with col2:

    st.subheader("📋 Job Description")

    job_description = st.text_area(
        "Paste the job description",
        height=220,
        placeholder=(
            "Paste the complete job description here..."
        )
    )


# ---------------------------------
# Analyze Button
# ---------------------------------

st.write("")

analyze_button = st.button(
    "🔍 Analyze Resume",
    type="primary",
    use_container_width=True
)


# ---------------------------------
# Analysis
# ---------------------------------

if analyze_button:

    # ---------------------------------
    # Validate Input
    # ---------------------------------

    if resume_file is None:

        st.warning(
            "⚠️ Please upload your resume PDF."
        )

        st.stop()

    if not job_description.strip():

        st.warning(
            "⚠️ Please paste a job description."
        )

        st.stop()


    # ---------------------------------
    # Extract Resume Text
    # ---------------------------------

    with st.spinner(
        "📖 Reading and analyzing your resume..."
    ):

        resume_text = extract_text_from_pdf(
            resume_file
        )


    if not resume_text.strip():

        st.error(
            "❌ Could not extract text from the resume."
        )

        st.stop()


    # ---------------------------------
    # Extract Skills
    # ---------------------------------

    resume_skills = extract_skills(
        resume_text
    )

    job_skills = extract_skills(
        job_description
    )


    # ---------------------------------
    # Compare Skills
    # ---------------------------------

    result = compare_skills(
        resume_skills,
        job_skills
    )

    matching_skills = result["matching_skills"]

    missing_skills = result["missing_skills"]

    match_score = result["match_score"]


    # ---------------------------------
    # Text Similarity
    # ---------------------------------

    similarity_score = calculate_similarity(
        resume_text,
        job_description
    )


    # ---------------------------------
    # ATS Analysis
    # ---------------------------------

    ats_result = analyze_ats(
        resume_text
    )

    ats_score = ats_result["ats_score"]

    ats_checks = ats_result["checks"]


    # ---------------------------------
    # Recommendations
    # ---------------------------------

    recommendations = generate_recommendations(
        missing_skills,
        ats_checks
    )


    # ---------------------------------
    # Results Header
    # ---------------------------------

    st.divider()

    st.header("📊 Resume Analysis Results")


    # ---------------------------------
    # Score Cards
    # ---------------------------------

    score1, score2, score3 = st.columns(3)

    with score1:

        st.metric(
            label="📊 Skill Match",
            value=f"{match_score}%"
        )

    with score2:

        st.metric(
            label="🤖 Text Similarity",
            value=f"{similarity_score}%"
        )

    with score3:

        st.metric(
            label="📋 ATS Checks",
            value=f"{ats_score}%"
        )


    # ---------------------------------
    # Progress Bars
    # ---------------------------------

    st.write("")

    p1, p2, p3 = st.columns(3)

    with p1:

        st.write("Skill Match")

        st.progress(
            int(match_score)
        )

    with p2:

        st.write("Resume–Job Similarity")

        st.progress(
            int(similarity_score)
        )

    with p3:

        st.write("Basic ATS Checks")

        st.progress(
            int(ats_score)
        )


    st.divider()


    # ---------------------------------
    # Tabs
    # ---------------------------------

    tab1, tab2, tab3 = st.tabs(
        [
            "🛠️ Skills Analysis",
            "📋 ATS Analysis",
            "💡 Recommendations"
        ]
    )


    # =================================
    # TAB 1 — Skills Analysis
    # =================================

    with tab1:

        st.subheader(
            "🛠️ Skills Analysis"
        )


        resume_col, job_col = st.columns(2)


        # ---------------------------------
        # Resume Skills
        # ---------------------------------

        with resume_col:

            st.markdown(
                "### 📄 Skills Found in Resume"
            )

            if resume_skills:

                for skill in resume_skills:

                    st.success(
                        skill.title()
                    )

            else:

                st.warning(
                    "No technical skills detected."
                )


        # ---------------------------------
        # Job Skills
        # ---------------------------------

        with job_col:

            st.markdown(
                "### 💼 Skills Required by Job"
            )

            if job_skills:

                for skill in job_skills:

                    st.info(
                        skill.title()
                    )

            else:

                st.warning(
                    "No known technical skills detected."
                )


        st.divider()


        # ---------------------------------
        # Matching Skills
        # ---------------------------------

        st.markdown(
            "### ✅ Matching Skills"
        )

        if matching_skills:

            st.success(
                ", ".join(
                    skill.title()
                    for skill in matching_skills
                )
            )

        else:

            st.info(
                "No matching skills found."
            )


        # ---------------------------------
        # Missing Skills
        # ---------------------------------

        st.markdown(
            "### ❌ Missing Skills"
        )

        if missing_skills:

            st.warning(
                ", ".join(
                    skill.title()
                    for skill in missing_skills
                )
            )

        else:

            st.success(
                "No missing skills detected."
            )


        st.divider()


        # ---------------------------------
        # Job Keyword Coverage
        # ---------------------------------

        st.markdown(
            "### 📌 Job Keyword Coverage"
        )

        total_job_skills = len(
            job_skills
        )

        matched_job_skills = len(
            matching_skills
        )

        if total_job_skills > 0:

            keyword_coverage = (
                matched_job_skills /
                total_job_skills
            ) * 100

            st.write(
                f"Your resume contains "
                f"{matched_job_skills} out of "
                f"{total_job_skills} technical skills "
                f"identified from the job description."
            )

            st.progress(
                int(keyword_coverage)
            )

            st.write(
                f"Keyword coverage: "
                f"{round(keyword_coverage, 2)}%"
            )

        else:

            st.info(
                "No technical skills were detected "
                "in the job description."
            )


    # =================================
    # TAB 2 — ATS Analysis
    # =================================

    with tab2:

        st.subheader(
            "📋 ATS Compatibility Analysis"
        )

        st.write(
            "These are basic keyword and structure "
            "checks designed to identify common "
            "resume elements."
        )


        for check, passed in ats_checks.items():

            if passed:

                st.success(
                    f"✓ {check}"
                )

            else:

                st.warning(
                    f"⚠️ {check} not detected"
                )


        st.divider()


        st.metric(
            "Basic ATS Check Score",
            f"{ats_score}%"
        )


    # =================================
    # TAB 3 — Recommendations
    # =================================

    with tab3:

        st.subheader(
            "💡 Resume Improvement Suggestions"
        )


        if recommendations:

            for i, recommendation in enumerate(
                recommendations,
                start=1
            ):

                st.info(
                    f"**{i}.** {recommendation}"
                )

        else:

            st.success(
                "No recommendations available."
            )


    # ---------------------------------
    # Extracted Resume Text
    # ---------------------------------

    st.divider()

    with st.expander(
        "📖 View Extracted Resume Text"
    ):

        st.text(
            resume_text
        )