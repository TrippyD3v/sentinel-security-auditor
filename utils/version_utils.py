def normalize_version(version):
    return [int(part) for part in version.split(".") if part.isdigit()]


def is_version_vulnerable(installed, affected):

    installed_parts = normalize_version(installed)
    affected_parts = normalize_version(affected)

    length = max(len(installed_parts), len(affected_parts))

    installed_parts += [0] * (length - len(installed_parts))
    affected_parts += [0] * (length - len(affected_parts))

    return installed_parts < affected_parts
