from __future__ import annotations 
import ast, sys 

class SymbolCollector(ast.NodeVisitor):
    def __init__(self) -> None:   
        self.table: dict[str, str] = {} 

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None: # 
        params = [
                ast.unparse(p.annotation) if p.annotation else "Any" 
                for p in node.args.args
            ]
        # 
