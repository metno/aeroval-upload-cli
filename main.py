import typer
import requests
from tusclient import client
from pathlib import Path
import magic
from typing_extensions import Annotated
from rich import print

TOKEN_URL = "http://localhost:8000/token"
UPLOAD_URL = "http://localhost:8080/files"

CHUNK_SIZE = 5 * 1024 * 1024  # 5 MB


def main(
    email: Annotated[str, typer.Option("--email", "-e", help="Email address")],
    password: Annotated[str, typer.Option("--password", "-p", help="Password")],
    files: Annotated[list[Path], typer.Option("--files", "-f", help="Files to upload")],
):
    token = get_token(email, password)
    uploaded_files = 0
    total_files = len(files)
    for file in files:
        is_allowed, mime_type = allowed_file(Path(file))
        if not is_allowed:
            print(f"[bold red]File {file} is not allowed.[/bold red]")
            continue
        upload_file(file, token, mime_type)
        uploaded_files += 1

    if uploaded_files == total_files:
        print(
            f"[bold green]All {total_files} files uploaded successfully.[/bold green]"
        )
    else:
        print(f"[bold red]Uploaded {uploaded_files} of {total_files} files.[/bold red]")


def get_token(email: str, password: str):
    response = requests.post(
        "http://localhost:8000/token", json={"username": email, "password": password}
    )
    response.raise_for_status()
    return response.json()


def allowed_file(file: Path) -> tuple[bool, str | None]:
    mime_type = magic.from_file(str(file), mime=True)
    if mime_type in [
        "application/x-netcdf",
        "application/netcdf",
        "application/x-hdf",
        "application/x-hdf5",
    ]:
        return True, mime_type
    return False, None


def upload_file(file: Path, token: dict, mime_type: str):
    tus = client.TusClient(
        UPLOAD_URL,
        headers={"Authorization": f"Bearer {token['access_token']}"},
    )
    uploader = tus.uploader(
        file_path=str(file),
        chunk_size=CHUNK_SIZE,
        retries=5,
    )
    uploader.metadata = {"filename": file.name, "filetype": mime_type}
    print(f"Uploading file {file}...")
    uploader.upload()

    print(f"[yellow]File {file} uploaded successfully.[/yellow]")


def app():
    typer.run(main)


if __name__ == "__main__":
    typer.run(main)
