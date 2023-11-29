import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("teste", "teste")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1, 1)

    assert encrypt_message("jaguara", 0) == "araugaj"
    assert encrypt_message("jaguara", 1) == "j_arauga"
