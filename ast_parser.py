import ast


class AssignmentFinder(ast.NodeVisitor):

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                print(
                    f"Variable: {target.id} | "
                    f"Line Number: {node.lineno}"
                )
            

        self.generic_visit(node)
    def visit_For(self, node):
        if isinstance(node.target,ast.Name):
            print(f"Variable:{node.target.id}|" f"Line Number:{node.lineno}")
        self.generic_visit(node)


with open("target_program.py", "r") as file:
    source_code = file.read()


tree = ast.parse(source_code)


finder = AssignmentFinder()
finder.visit(tree)