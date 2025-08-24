import pytest
import json
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    """Test the home endpoint."""
    response = client.get('/')
    assert response.status_code == 200
    
    data = response.get_json()
    assert 'message' in data
    assert data['message'] == 'Secure CI/CD Demo'

def test_health_endpoint(client):
    """Test the health check endpoint."""
    response = client.get('/health')
    assert response.status_code == 200
    
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert 'checks' in data

def test_security_headers():
    """Ensure no sensitive data is exposed."""
    with app.test_client() as client:
        response = client.get('/')
        
        # Check that response doesn't contain sensitive patterns
        response_text = str(response.data)
        
        # These should not appear in any response
        forbidden_patterns = ['password', 'secret', 'token', 'key']
        for pattern in forbidden_patterns:
            assert pattern.lower() not in response_text.lower(), f"Found {pattern} in response"