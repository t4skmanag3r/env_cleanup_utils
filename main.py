import argparse
import os
import logging
import sys
from typing import Callable
from env_cleanup_utils import (
    find_venv_dirs,
    find_pycache_dirs,
    find_node_modules_dirs,
    save_requirements,
    delete_venv,
    delete_pycache,
    delete_node_modules,
    testing,
    logger,
    PipNotFoundError,
)


def ask_for_confirmation(dir_path: str, delete_func: Callable):
    answer = ""
    while answer not in ["y", "n"]:
        answer = input(f"Are you sure you want to delete: {dir_path} [y/n]? ")
    if answer == "y":
        delete_func(dir_path)
    elif answer == "n":
        return


def main():
    parser = argparse.ArgumentParser(
        description="Cleanup python virtual environments (venv), __pycache__, node_modules dirrectories and save requirements.txt for entire dirrectory trees"
    )
    parser.add_argument("root_dir", help="Root directory to search for venvs")
    parser.add_argument(
        "--delete-all",
        action="store_true",
        help="Delete everything (venv, pycache, node_modules)",
    )
    parser.add_argument("--delete-venv", action="store_true", help="Delete venvs")
    parser.add_argument(
        "--delete-pycache",
        action="store_true",
        help="Delete pycache directories, cofirmed automatically",
    )
    parser.add_argument(
        "--delete-node", action="store_true", help="Delete node_modules directories"
    )
    parser.add_argument(
        "-y",
        action="store_true",
        help="Yes to all, auto confirm all venv & node_modules deletion prompts",
    )
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")

    args = parser.parse_args()

    if args.debug:
        logger.setLevel(logging.DEBUG)

    try:
        venv_dirs = find_venv_dirs(args.root_dir)

        for venv_dir in venv_dirs:
            print(f"Found venv in directory: {venv_dir}")
            save_requirements(venv_dir)
            print(
                f"Requirements frozen to {os.path.join(os.path.dirname(venv_dir), 'requirements.txt')}"
            )

            if args.delete_venv or args.delete_all:
                if args.y:
                    delete_venv(venv_dir)
                    print(f"Deleted venv in directory: {venv_dir}")
                else:
                    ask_for_confirmation(venv_dir, delete_venv)

        if args.delete_pycache or args.delete_all:
            pycache_dirs = find_pycache_dirs(args.root_dir)
            for pycache in pycache_dirs:
                delete_pycache(pycache)

        if args.delete_node or args.delete_all:
            node_dirs = find_node_modules_dirs(args.root_dir)
            for node_dir in node_dirs:
                if args.y:
                    print(f"Deleted node_modules in directory: {node_dir}")
                    delete_node_modules(node_dir)
                else:
                    ask_for_confirmation(node_dir, delete_node_modules)

    except PermissionError:
        print(
            "ERROR: Unable to access dirrectories, please close any open dirrectories before running"
        )
        sys.exit(1)

    except PipNotFoundError as e:
        print(e)
        sys.exit(1)

    except Exception as e:
        if args.debug:
            raise e
        else:
            print(e)
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    # root_folder = "./sample_folder"
    # testing.create_sample_folder_structure(root_folder)
    # testing.create_virtual_environment(os.path.join(root_folder, "project1", ".venv"))
    # testing.create_virtual_environment(os.path.join(root_folder, "project2", "venv"))
    ## poetry run python main.py "./sample_folder" --delete-venv --debug
    main()
