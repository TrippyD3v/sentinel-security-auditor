def print_findings(findings):

    if not findings:
        print("\nNo vulnerabilities detected.")
        return

    print("\nVulnerability Findings:\n")

    for finding in findings:

        print(
            f"[{finding.severity}] {finding.package} {finding.version} → {finding.cve_id}"
        )
