import pytest

def test_inverter_string():
  assert(inverter_string("Brasil")) == "O inverso da palavra Brasil é lisarB."

  assert(inverter_string("oi")) == "O inverso da palavra oi é io."

  assert(inverter_string("Botafogo")) == "O inverso da palavra Botafogo é ogofatoB."

  assert(inverter_string("Predio")) == "O inverso da palavra Predio é oiderP."

  assert(inverter_string("Casa")) == "O inverso da palavra Casa é asaC."
  

if __name__ == "__main__":
    pytest.main(['-svv', __file__])
