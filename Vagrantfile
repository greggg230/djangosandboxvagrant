# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
    config.vm.define "web" do |web|
        web.vm.box = "centos/7"
        web.vm.network "forwarded_port", guest: 8318, host: 8318, host_ip: "127.0.0.1"
        web.vm.network "forwarded_port", guest: 8319, host: 8319, host_ip: "127.0.0.1"
        web.vm.provision :ansible_local do |ansible|
            ansible.playbook = "playbook.yml"
        end
    end
end
