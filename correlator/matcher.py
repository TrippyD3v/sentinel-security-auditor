from models.data_models import Package, VulnerabilityFinding
from utils.version_utils import is_version_vulnerable
from utils.severity_utils import extract_severity


def match_packages_to_cves(packages, cves):

    findings = []

    for pkg in packages:

        for cve in cves:

            cve_data = cve["cve"]

            descriptions = cve_data["descriptions"]

            description_text = descriptions[0]["value"].lower()

            severity = extract_severity(cve_data)

            if pkg.name.lower() in description_text:

                findings.append(
                    VulnerabilityFinding(
                        package=pkg.name,
                        version=pkg.version,
                        cve_id=cve_data["id"],
                        severity=severity
                    )
                )

    return findings
