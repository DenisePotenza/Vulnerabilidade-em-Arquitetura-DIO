def build_stride_prompt(extracted_text: str) -> str:
    return f"""You are a cybersecurity assistant. Perform a STRIDE analysis.

System description:
{extracted_text}

Return threats categorized under:
- Spoofing
- Tampering
- Repudiation
- Information Disclosure
- Denial of Service
- Elevation of Privilege

For each component, provide: threat, likelihood, impact, and recommended mitigation.
Return the answer in JSON format.
"""
