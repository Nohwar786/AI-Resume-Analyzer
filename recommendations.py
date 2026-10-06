def generate_recommendations(
    missing_skills,
    ats_checks
):
    """
    Generate resume improvement recommendations
    based on missing job skills and ATS checks.
    """

    recommendations = []


    # ---------------------------------
    # Missing Skills
    # ---------------------------------

    if missing_skills:

        skills = ", ".join(
            skill.title()
            for skill in missing_skills
        )

        recommendations.append(
            f"Consider adding relevant skills "
            f"from the job description if you "
            f"genuinely have experience with them: "
            f"{skills}."
        )


    # ---------------------------------
    # ATS Checks
    # ---------------------------------

    if not ats_checks.get(
        "Contact Information",
        False
    ):

        recommendations.append(
            "Add clear contact information, "
            "including your email address and "
            "phone number."
        )


    if not ats_checks.get(
        "Education",
        False
    ):

        recommendations.append(
            "Add a clear Education section "
            "with your degree and institution."
        )


    if not ats_checks.get(
        "Experience / Internship",
        False
    ):

        recommendations.append(
            "Add relevant internship or work "
            "experience if applicable."
        )


    if not ats_checks.get(
        "Projects",
        False
    ):

        recommendations.append(
            "Add a Projects section describing "
            "your technical projects."
        )


    if not ats_checks.get(
        "Skills Section",
        False
    ):

        recommendations.append(
            "Add a clearly labeled Technical "
            "Skills section."
        )


    if not ats_checks.get(
        "Certifications",
        False
    ):

        recommendations.append(
            "Add relevant certifications if "
            "you have completed any."
        )


    if not ats_checks.get(
        "Quantifiable Achievements",
        False
    ):

        recommendations.append(
            "Add measurable results to your "
            "project or experience descriptions "
            "where possible, such as percentages, "
            "numbers, or performance improvements."
        )


    if not ats_checks.get(
        "Action-Oriented Content",
        False
    ):

        recommendations.append(
            "Use strong action verbs such as "
            "Developed, Implemented, Designed, "
            "Built, and Optimized in your resume."
        )


    if not ats_checks.get(
        "Readable Resume Length",
        False
    ):

        recommendations.append(
            "Review the resume length and keep "
            "the content concise and focused."
        )


    # ---------------------------------
    # Default Recommendation
    # ---------------------------------

    if not recommendations:

        recommendations.append(
            "Your resume passed the basic ATS "
            "checks. Continue tailoring the resume "
            "to each job description."
        )


    return recommendations