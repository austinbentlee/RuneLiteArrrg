import os
import subprocess

jre_path = "C:\\Program Files\\Java\\jre1.8.0_241\\bin\\java.exe" #path to java exe
ram_allocation = "2048m" #how much ram to use in mb
runelite_path = os.environ.get('USERPROFILE') + "\\AppData\\Local\\RuneLite\\" #shouldn't ever have to change

jarPath = runelite_path + "runelite.jar"
command = "\"" + jre_path + "\"" + "  -jar " + "\""+jarPath+"\""
print(command)
out = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
stdout, _ = out.communicate()

print("\r\n\r\n")

stdout = str(stdout)
stdout = stdout.split("\\r\\n")
runningLine = None

for line in stdout:
	if "Running" in line:
		runningLine = line
		
		
if runningLine is None:
	print("Could not update launcher.")
	
runningLine = str(runningLine)
runningLine = runningLine.replace("\\\\", "\\").replace("\\\\", "\\").replace("\\\\", "\\").replace("\\\\", "\\")
args = runningLine.split("[")[2].split(",")
jars = args[2].replace(" ", "")
version = args[len(args) - 2].split("=")[1]
print(jars)
print(version)


output = "\"" + jre_path + "\" -cp \"" + jars + "\" -XX:+DisableAttachMechanism -Xmn" + ram_allocation + " -Xmx" + ram_allocation + " -Xss32m -XX:CompileThreshold=15000 -Xincgc -XX:+UseParNewGC -Djna.nosys=true -Dsun.java2d.noddraw=false -Dsun.java2d.opengl=false -Djava.net.preferIPv4Stack=true -Djava.net.preferIPv4Addresses=true -XX:+AlwaysPreTouch -XX:+UseFastAccessorMethods -XX:AllocatePrefetchStyle=2 -XX:ReservedCodeCacheSize=128m -Drunelite.launcher.version="+version+" net.runelite.client.RuneLite"

with open("launcher.bat", "w") as f:
	f.write(output)
	
print("Done. Close runelite and start launcher.bat.")