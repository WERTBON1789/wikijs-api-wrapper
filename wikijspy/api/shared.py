from typing import Tuple

def _generate_output_str(output) -> str:
    if type(output[0]) is str:
        output_str: str = ""
        for item in output:
            output_str += item+","
        return output_str
    if isinstance(output[0], Tuple):
        output_str: str = ""
        output_dict: Tuple[str, str] = {}
        
        for item in output:
            if output_dict.get(item[0]) is None:
                output_dict[item[0]] = []
            output_dict[item[0]].append(item[1])
        
        for key,val in output_dict.items():
            if not val:
                continue
            
            output_str += key+'{'
            
            for item in val:
                output_str += item+','
            output_str += '}'
        return output_str
