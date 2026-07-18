from agri_platform.orchestration.coordinator import AgentCoordinator
from agri_platform.orchestration.weather_agent import WeatherAgent
def test_run():
 c=AgentCoordinator([WeatherAgent()])
 assert len(c.run({'rainfall_forecast':25}))==1
