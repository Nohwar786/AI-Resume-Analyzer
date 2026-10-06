from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def compare_skills(resume_skills, job_skills):
    """
    Compare resume skills with skills required by the job.
    """

    resume_set = set(resume_skills)
    job_set = set(job_skills)

    matching_skills = sorted(
        resume_set.intersection(job_set)
    )

    missing_skills = sorted(
        job_set - resume_set
    )

    if job_set:
        match_score = (
            len(matching_skills) / len(job_set)
        ) * 100
    else:
        match_score = 0

    return {
        "matching_skills": matching_skills,
        "missing_skills": missing_skills,
        "match_score": round(match_score, 2)
    }


def calculate_similarity(resume_text, job_description):
    """
    Calculate similarity between the resume
    and job description using TF-IDF.
    """

    documents = [
        resume_text,
        job_description
    ]

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    tfidf_matrix = vectorizer.fit_transform(
        documents
    )

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0]

    return round(
        similarity * 100,
        2
    )