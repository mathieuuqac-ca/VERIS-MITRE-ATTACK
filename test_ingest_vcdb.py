from pathlib import Path

from e3_pipeline.ingest_vcdb import extract_leaf_paths, normalize_incident


def test_extract_leaf_paths():
    obj = {"social": {"vector": {"phishing": True, "other": False}}}
    result = extract_leaf_paths(obj)

    assert "social.vector.phishing" in result
    assert "social.vector.other" not in result


def test_normalize_incident_minimal():
    data = {
        "incident_id": "INC-001",
        "summary": "Incident de test avec une description assez longue pour être conservée.",
        "actor": {"external": True},
        "action": {"social": {"vector": {"phishing": True}}},
        "asset": {"server": True},
        "attribute": {"confidentiality": {"data_disclosure": True}},
    }

    incident = normalize_incident(data, Path("fake.json"))

    assert incident.incident_id == "INC-001"
    assert "external" in incident.veris_actor
    assert "social.vector.phishing" in incident.veris_action
