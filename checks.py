# coding: utf-8

from pathlib import Path
import os
import time


from ipmrunner.checks import requirement


@requirement("Es posible ejecutar \"{filename}\" con el locale \"{locale}\"")
def ejecutar_con_locale(fixtures, filename, locale):
    file = Path.cwd() / filaname
    env = dict(LC_ALL= locale, LANG= locale, LANGUAGE= locale)
    app = fixtures.AtspiApplication(file)
    app.run(env= env)
    time.sleep(0.5)
    assert app.is_running()
    app.stop()

@requirement("PlantUML compila correctamente los ficheros \"{glob}\""](check:)
def plantuml_compiles(fixtures, glob):
    plantuml = fixtures.Command("plantuml", cwd= Path.cwd())
    for file in Path.cwd().glob(glob):
        result = plantuml("-checkonly", "-v", str(file))
        assert "Number of image(s): 0" not in result.stdout, f"El fichero {str(file)} no genera ninguna imagen"

@requirement("Después de ejecutar \"{filename}\", se muestra una ventana \"{wname}\"")
def cerrar_termina(fixtures, filename, wname):
    file = Path.cwd() / filename
    app = fixtures.AtspiApplication(file)
    app.run()
    w = app.children.first(role= 'FRAME', name= wname)
    app.stop()
    assert w is not None

@requirement("Los ficheros \"{glob}\" están actualizados respecto a la versión \"{tag}\"")
def files_have_diff(fixtures, glob, tag):
    files = Path.cwd().glob(glob)
    if all(file for file in files if fixtures.git.diff("HEAD", tag, str(file)) == ""):
        assert False "", f"No hay ningún fichero en {glob} actualizado desde la versión {tag}"
        
@requirement("El fichero \"{filename}\" está actualizado respecto a la versión \"{tag}\"")
def file_has_diff(fixtures, filename, tag):
    diff = fixtures.git.diff("HEAD", tag, filename)
    assert diff != ""
    
@requirement("Existe un único fichero \"{filename}\"")
def file_is_unique(fixtures, filename):
    def is_unique_at(file, dir):
        for child in dir.iterdir():
            if child.name.startswith(".git") or child == file:
                continue
            if child.is_dir() and is_unique_at(file, child):
                continue
            return False
        return True

    file = Path.cwd() / filename
    assert file.is_file()
    assert is_unique_at(file, Path.cwd(), f"Hay ficheros adicionales: {child.name}"
        
@requirement("Existe al menos un fichero \"{glob}\" en el directorio \"{dirname}\"")
def non_empty(fixtures, glob, dirname):
    dir = Path.cwd() / dirname
    assert dir.is_dir()
    assert len(list(dir.glob(glob))) > 0, f"No hay ficheros {glob} en {dirname}"
    
@requirement("Existe un fichero \"{filename}\"")
def existe(fixtures, filename):
    file = Path.cwd() / filename
    assert file.is_file()

@requirement("Existe un fichero \"{filename}\" y es ejecutable")
def es_ejecutable(fixtures, filename):
    file = Path.cwd() / filename
    assert os.access(file, os.X_OK)

@requirement("No hay ficheros pendientes de commit")
def nothing_to_commit(fixtures):
    assert fixtures.git.status() == []

@requirement("El último commit tiene la etiqueta \"{tagname}\"")
def tiene_etiqueta(fixtures, tagname):
    tags = fixtures.git.tag("--contains", "HEAD")
    assert tagname in tags

@requirement("El nombre del repositorio remote es \"{remote_name}\"")
def el_remote_es(fixtures, remote_name):
    assert remote_name in fixtures.git.remote()


@requirement("El repositorio remote \"{remote_name}\" está actualizado")
def el_remote_esta_up_to_date(fixtures, remote_name):
    branches = fixtures.git.branch()
    current_branches = [ branch[2:] for branch in branches if branch.startswith("* ")]
    if len(current_branches) != 1:
        raise RuntimeError(f"Git reported 1>n>1 current branches. {branches}")
    branch_name = current_branches[0]
    try:
        assert fixtures.git.push("-n", remote_name, branch_name) == "Everything up-to-date"
        assert fixtures.git.push("-n", "--tags", remote_name, branch_name) == "Everything up-to-date"
    except OSError as e:
        assert False, str(e)
