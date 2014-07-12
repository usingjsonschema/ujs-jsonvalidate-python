"""
Unit tests for jsonValidate.
"""
from jsonvalidate import validate, VALID, INVALID_JSON, MISSING_ID, VALIDATION_ERROR
from safefile import DOES_NOT_EXIST, INVALID_NAME

class TestValidate:
    # process before each test method
    def setup_method (self, method):
        pass

    # clean up after each test method
    def teardown_method (self, method):
        pass

    def test_does_not_exist_data (self):
        code, data, message = validate ("test/nofile.json", "test/schema1.json", None, None)
        assert code == DOES_NOT_EXIST

    def test_does_not_exist_schema (self):
        code, data, message = validate ("test/valid1.json", "test/nofile.json", None, None)
        assert code == DOES_NOT_EXIST

    def test_does_not_exist_ref (self):
        code, data, message = validate ("test/valid1.json", "test/schema1.json", ["test/nofile.json"], None)
        assert code == DOES_NOT_EXIST

    def test_does_not_exist_jsdb (self):
        code, data, message = validate ("test/valid1.json", "test/schema1.json", None, "test/nofile.json")
        assert code == DOES_NOT_EXIST

    def test_invalid_name_data (self):
        code, data, message = validate (None, "test/schema1.json", None, None)
        assert code == INVALID_NAME

    def test_invalid_name_schema (self):
        code, data, message = validate ("test/valid1.json", None, None, None)
        assert code == INVALID_NAME

    def test_invalid_json_data (self):
        code, data, message = validate ("test/invalid.json", "test/schema1.json", None, None)
        assert code == INVALID_JSON

    def test_invalid_json_schema (self):
        code, data, message = validate ("test/valid1.json", "test/invalid.json", None, None)
        assert code == INVALID_JSON

    def test_invalid_json_ref (self):
        code, data, message = validate ("test/valid1.json", "test/schema1.json", ["test/invalid.json"], None)
        assert code == INVALID_JSON

    def test_invalid_json_jsdb (self):
        code, data, message = validate ("test/valid1.json", "test/schema1.json", None, "test/invalid.json")
        assert code == INVALID_JSON

    def test_missing_id (self):
        code, data, message = validate ("test/valid1.json", "test/schema1.json", ["test/valid1.json"], None)
        assert code == MISSING_ID

    def test_valid (self):
        code, data, message = validate ("test/valid1.json", "test/schema1.json", None, None)
        assert code == VALID

    def test_valid_with_ref (self):
        code, data, message = validate ("test/valid2.json", "test/schema2.json", ["test/ref2.json"], None)
        assert code == VALID

    def test_valid_with_jsdb (self):
        code, data, message = validate ("test/valid3.json", "test/schema3.json", None, "test/jsdb3.json")
        assert code == VALID

    def test_invalid (self):
        code, data, message = validate ("test/invalid1.json", "test/schema1.json", None, None)
        assert code == VALIDATION_ERROR

    def test_invalid_with_ref (self):
        code, data, message = validate ("test/invalid2.json", "test/schema2.json", ["test/ref2.json"], None)
        assert code == VALIDATION_ERROR

    def test_invalid_with_jsdb (self):
        code, data, message = validate ("test/invalid3.json", "test/schema3.json", None, "test/jsdb3.json")
        assert code == VALIDATION_ERROR

    def test_valid_with_3_level_jsdb (self):
        code, data, message = validate ("test/valid4.json", "test/schema4.json", None, "test/jsdb4.json")
        assert code == VALID

    def test_invalid_with_3_level_jsdb (self):
        code, data, message = validate ("test/invalid4.json", "test/schema4.json", None, "test/jsdb4.json")
        assert code == VALIDATION_ERROR
