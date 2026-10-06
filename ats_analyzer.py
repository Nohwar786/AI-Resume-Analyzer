import re


def analyze_ats(resume_text):
    """
    Analyze basic ATS-friendly characteristics
    of a resume using keyword and structure checks.
    """

    text = resume_text.lower()

    checks = {}


    # ---------------------------------
    # 1. Contact Information
    # ---------------------------------

    email_found = bool(
        re.search(
            r"\b[\w.-]+@[\w.-]+\.\w+\b",
            text
        )
    )

    phone_found = bool(
        re.search(
            r"\b\d{10}\b",
            re.sub(r"\D", "", text)
        )
    )

    checks["Contact Information"] = (
        email_found and phone_found
    )


    # ---------------------------------
    # 2. Education
    # ---------------------------------

    education_keywords = [
        "education",
        "b.tech",
        "bachelor",
        "degree",
        "university",
        "college"
    ]

    checks["Education"] = any(
        keyword in text
        for keyword in education_keywords
    )


    # ---------------------------------
    # 3. Skills Section
    # ---------------------------------

    skills_keywords = [
        "technical skill",
        "skills",
        "technologies",
        "programming languages"
    ]

    checks["Skills Section"] = any(
        keyword in text
        for keyword in skills_keywords
    )


    # ---------------------------------
    # 4. Projects
    # ---------------------------------

    project_keywords = [
        "projects",
        "project",
        "developed",
        "implemented"
    ]

    checks["Projects"] = any(
        keyword in text
        for keyword in project_keywords
    )


    # ---------------------------------
    # 5. Experience / Internship
    # ---------------------------------

    experience_keywords = [
        "experience",
        "work experience",
        "internship",
        "intern"
    ]

    checks["Experience / Internship"] = any(
        keyword in text
        for keyword in experience_keywords
    )


    # ---------------------------------
    # 6. Certifications
    # ---------------------------------

    certification_keywords = [
        "certification",
        "certifications",
        "certificate"
    ]

    checks["Certifications"] = any(
        keyword in text
        for keyword in certification_keywords
    )


    # ---------------------------------
    # 7. Quantifiable Achievements
    # ---------------------------------

    number_patterns = [
        r"\b\d+%",
        r"\b\d+\+",
        r"\b\d+\s*(users|projects|records|students|clients)"
    ]

    achievement_found = any(
        re.search(pattern, text)
        for pattern in number_patterns
    )

    checks["Quantifiable Achievements"] = (
        achievement_found
    )


    # ---------------------------------
    # 8. Action Verbs
    # ---------------------------------

    action_verbs = [
        "developed",
        "implemented",
        "designed",
        "created",
        "analyzed",
        "managed",
        "built",
        "configured",
        "optimized"
    ]

    action_verb_count = sum(
        text.count(verb)
        for verb in action_verbs
    )

    checks["Action-Oriented Content"] = (
        action_verb_count >= 2
    )


    # ---------------------------------
    # 9. Resume Length
    # ---------------------------------

    word_count = len(
        text.split()
    )

    checks["Readable Resume Length"] = (
        200 <= word_count <= 1500
    )


    # ---------------------------------
    # Calculate ATS Score
    # ---------------------------------

    passed_checks = sum(
        checks.values()
    )

    total_checks = len(
        checks
    )

    ats_score = (
        passed_checks /
        total_checks
    ) * 100


    return {
        "checks": checks,
        "ats_score": round(
            ats_score,
            2
        )
    }