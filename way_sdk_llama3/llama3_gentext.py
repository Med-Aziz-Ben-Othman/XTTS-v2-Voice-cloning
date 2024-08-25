import os
import sys

# Adjust the sys.path to include the way-sdk directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'way-sdk')))

from way_llm_model.LL_model import LL_model

class llama3_gentext:
    def __init__(self, model_name, modelfilepath):
            self.model_name = model_name
            self.modelfilepath = modelfilepath
            self.model_check_file = f"{self.model_name}.txt"

    def create_model_if_needed(self):
            if os.path.exists(self.model_check_file):
                print(f"Model '{self.model_name}' already exists. Skipping creation.")
            else:
                LL_model.create(model_name=self.model_name, modelfilepath=self.modelfilepath)
                with open(self.model_check_file, 'w') as f:
                    f.write(f"Model '{self.model_name}' created.")

    def generate_response(self, prompt, output_file):
        # Generate the response using the model
        response = LL_model.generate(model=self.model_name, prompt=prompt)
        
        # Ensure the response is a string and encode it in UTF-8 before writing to the file
        if isinstance(response, bytes):
            # If the response is in bytes, decode it to a string
            response = response.decode('utf-8')
        
        # Write the response to the output file with UTF-8 encoding
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(response)
        
        # Optionally print and return the response
        print(f"Generated response: {response}")
        return response
