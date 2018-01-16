# Module: MetaQUAST (Quast)
def commence(action):
	import subprocess, os
	if action == 'check':
		try:
			if os.path.isfile('./quast/install_log.stdout'):
				return True
			else:
				return False
		except Exception as e:
			return e

	if action == 'install':
		try:
			print "\tInstalling Quast..."
			FNULL = open(os.devnull, 'w')
			print "\t\tCloning from git..."
			subprocess.call(["git", "clone", "https://github.com/ablab/quast.git"], stdout=FNULL, stderr=FNULL)
			os.chdir('quast')
			print "\t\tBuilding..."
			subprocess.call(['./install_full.sh'], stdout=FNULL, stderr=FNULL, close_fds=True, shell=True)
			path = os.getcwd()
			os.chdir('..')
			print "\t\tWriting paths to PATH_additions.txt..."
			with open("SfB_path_additions.txt", "a") as source:
				source.write('export PATH='+path+':$PATH'+"\n")
			# deps: git, make(gcc)
			print "\t\tSuccess."
		except Exception as e:
			print "WARNING: MetaQUAST - This deployment module needs an update or dependenciess are not met. Caught exception: "+str(e)

if __name__ == '__main__':
	# Check if installed (exists in PATH) 
	installed = commence('check')
	# Install
	if installed != True:
		pass
		commence('install')
	else:
		print "Megahit is already installed."
