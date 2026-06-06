def calulate_risk(score):
  if score > 70:
    return "High"
    return "Low"

def test_calculate_risk():
  assert calclulate_risk(85) == "High"
  assert calculate_risk(50) == "Low"
print("All tests passed successfully")

if __name__ == "--main--":
  test_calculate_risk()
