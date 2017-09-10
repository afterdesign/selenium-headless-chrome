Vagrant.configure('2') do |config|
    config.vm.provider 'virtualbox' do |v|
        v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    end

    config.vm.box = "debian/stretch64"

    config.vm.network 'private_network', ip: '192.192.1.201'

    config.vm.synced_folder '.', '/project', type: 'nfs', mount_options: ['actimeo=1', 'vers=3']

    config.vm.provision "ansible_local" do |ansible|
        ansible.provisioning_path = "/project"
        ansible.playbook = "vagrant/playbook.yml"
        ansible.install_mode = "pip"
    end
end
