# This guide is optimized for Vagrant 1.7 and above.
# Although versions 1.6.x should behave very similarly, it is recommended
# to upgrade instead of disabling the requirement below.

Vagrant.require_version ">= 1.7.0"

Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/xenial64"
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.network "private_network", ip: "192.168.33.13"
  config.vm.hostname = "mbf"

  config.vm.synced_folder ".", "/mbf"

  config.vm.provision "ansible" do |ansible|
    ansible.verbose = "v"
    ansible.playbook = "playbook.yml"
    ansible.raw_arguments = ["--vault-password-file=.vault_pass.txt"]
  end
end
