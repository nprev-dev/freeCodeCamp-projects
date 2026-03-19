test_settings = {
    'theme': 'dark',
    'notifications': 'enabled'
}

def add_setting(settings, pair):
    key, value = pair     # unpack pair
    
    key = key.lower()     #puts to lowercase
    value = value.lower() #puts to lowercase
    
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, pair):
    key, value = pair        #unpack pair
    
    key = key.lower()        #puts to lowercase
    value = value.lower()    #puts to lowercase

    if key in settings:
        settings[key] = value # adds key value pair to dict
        return f"Setting '{key}' updated to '{value}' successfully!"
    if key not in settings:
        return  f"Setting '{key}' does not exist! Cannot update a non-existing setting."
def delete_setting(settings, key):
    key = key.lower()         # puts to lowercase
    if key in settings:
       del settings[key]
       return f"Setting '{key}' deleted successfully!" 
    if key not in settings:
        return f"Setting not found!"
def view_settings(settings):
    if settings == {}:         #if setting dict empty
        return "No settings available."
    if settings:
        result = "Current User Settings:"
        
        for key, value in settings.items(): #loops through all key-value pairs in settings
            result += f"\n{key.capitalize()}: {value}"
        
        return result + '\n'
