progName={
    "Hamza":{
        "python":"100%",
        "HTML":"70%",
        "CSS":"90%"

    },
    "Lulia":{
       "python":"10%",
        "HTML":"77%",
        "CSS":"20%"  

    },
    "Sobhia":{
        "python":"50%",
        "HTML":"66%",
        "CSS":"90%"
    }

}
#print(progName["Hamza"]["python"])
for name in progName:
    print(f"the programer name is: {name} and the level of: ")
    for levelLang in progName[name]:
       print(f"{levelLang} ==> {progName[name][levelLang]}")

