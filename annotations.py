import ast, sys, pprint 

def main(path: str) -> None:
    src = open(path, encoding="utf-8").read()
    tree = ast.parse(src, filename=path, type_comments=True)
    pprint.pp(ast.dump(tree,indent=4))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("u forgor the other arg vro")
        raise SystemExit(1)
    main(sys.argv[1])
 
