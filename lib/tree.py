class Tree:
    def __init__(self, root):
        self.root = root

    def get_element_by_id(self, target_id):
        def traverse(node):
            if node['id'] == target_id:
                return node
            for child in node['children']:
                result = traverse(child)
                if result:
                    return result
            return None

        return traverse(self.root)
