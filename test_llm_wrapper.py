import json

from e3_pipeline.llm_wrapper import extract_json_object, mock_llm_response, parse_and_validate


def test_extract_json_object_direct():
    data = extract_json_object('{"incident_id": "1", "confidence": 0.5}')
    assert data["incident_id"] == "1"


def test_mock_response_valid():
    incident = {
        "incident_id": "INC-001",
        "veris_action": ["social.vector.phishing"],
    }
    raw = mock_llm_response(incident)
    parsed = json.loads(raw)

    assert parsed["incident_id"] == "INC-001"
    assert "T1566" in parsed["predicted_attack_ids"]


def test_parse_and_validate():
    raw = '''
    {
      "incident_id": "INC-001",
      "predicted_attack_ids": ["T1566"],
      "confidence": 0.7,
      "justification": "Phishing probable.",
      "matched_veris_fields": ["social.vector.phishing"]
    }
    '''
    parsed = parse_and_validate(raw, "INC-001")

    assert parsed["incident_id"] == "INC-001"
    assert parsed["confidence"] == 0.7
