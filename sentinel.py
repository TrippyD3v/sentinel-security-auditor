from scanner.package_scanner import get_installed_packages
from vulnerability.cve_client import fetch_recent_cves
from correlator.matcher import match_packages_to_cves
from reporting.reporter import print_findings


def main():

    print("Scanning system packages...")

    packages = get_installed_packages()

    print("Packages discovered:", len(packages))


    print("\nDownloading CVE intelligence...")

    cves = fetch_recent_cves(50)

    print("CVE records retrieved:", len(cves))


    print("\nRunning vulnerability correlation...")

    findings = match_packages_to_cves(packages, cves)

    print_findings(findings)


if __name__ == "__main__":
    main()
