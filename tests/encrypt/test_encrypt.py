from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():

    assert encrypt_message("segundo_indice", 2) == "ecidni_odnug_es"
    assert encrypt_message("primeiro_indice", 1) == "p_ecidni_oriemir"
    assert encrypt_message("maior_key", 11) == "yek_roiam"

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("sem", "number")  # apenas string

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(555555555, 6)  # apenas number
