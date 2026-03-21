def extract_severity(cve):

    metrics = cve.get("metrics", {})

    if "cvssMetricV31" in metrics:

        cvss_data = metrics["cvssMetricV31"][0]

        severity = cvss_data["cvssData"]["baseSeverity"]

        return severity

    return "UNKNOWN"
