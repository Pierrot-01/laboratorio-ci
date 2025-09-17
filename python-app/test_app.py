from app import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hola Mundo" in captured.out

