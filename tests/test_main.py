from catdir.main import handler as catdir


def test_basic_run(tmp_path, capsys):
    file = tmp_path / "example.txt"
    file.write_text("hello")

    catdir(str(tmp_path), exclude=[], exclude_noise=False)
    out = capsys.readouterr().out
    assert "hello" in out


def test_exclude_file(tmp_path, capsys):
    (tmp_path / "keep.txt").write_text("keep")
    (tmp_path / "ignore.txt").write_text("ignore")

    catdir(str(tmp_path), exclude=["ignore.txt"], exclude_noise=False)
    out = capsys.readouterr().out
    assert "keep" in out
    assert "ignore" not in out


def test_subdirectory(tmp_path, capsys):
    subdir = tmp_path / "sub"
    subdir.mkdir()
    (subdir / "a.txt").write_text("subfile")

    catdir(str(tmp_path), exclude=[], exclude_noise=False)
    out = capsys.readouterr().out
    assert "subfile" in out


def test_read_error(tmp_path, capsys):
    secret = tmp_path / "secret.txt"
    secret.write_text("can't read")
    secret.chmod(0)

    try:
        catdir(str(tmp_path), exclude=[], exclude_noise=False)
    finally:
        secret.chmod(0o644)

    out = capsys.readouterr().out
    assert "error while reading" in out
