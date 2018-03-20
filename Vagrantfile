# This guide is optimized for Vagrant 1.7 and above.
# Although versions 1.6.x should behave very similarly, it is recommended
# to upgrade instead of disabling the requirement below.

Vagrant.require_version ">= 1.7.0"

Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/xenial64"
  config.vm.network "forwarded_port", guest: 9000, host: 9000
  config.vm.hostname = "better-spots"

  config.vm.synced_folder ".", "/better_spots"

  config.vm.provision "ansible" do |ansible|
    ansible.verbose = "v"
    ansible.playbook = "playbook.yml"
    ansible.raw_arguments = ["--vault-password-file=.vault_pass.txt"]
    ansible.skip_tags = ENV['SKIP_TAGS']
    ansible.tags = ENV['TAGS']
  end

    config.vm.provider "virtualbox" do |vb|
        vb.memory = 4096
        vb.cpus = 2
    end

end
