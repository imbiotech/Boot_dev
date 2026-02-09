def count_marketers(job_titles):
    return job_titles.count("marketer")

    return sum(
        1
        for job in job_titles
        if job.lower() == "marketer"
    )


