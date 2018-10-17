import pytest
import json


class TestOsdsFromMons(object):
    @pytest.mark.no_docker
    def test_all_osds_are_up_and_in(self, node, host):
        cmd = "sudo ceph --cluster={cluster} --connect-timeout 5 -s -f json".format(cluster=node["cluster_name"])
        output = json.loads(host.check_output(cmd))
        assert status['osdmap']['osdmap']['num_osds'] == status['osdmap']['osdmap']['num_up_osds']

    @pytest.mark.docker
    def test_all_docker_osds_are_up_and_in(self, node, host):
        cmd = "sudo docker exec ceph-mon-{inventory_hostname} ceph --cluster={cluster} --connect-timeout 5 -s -f json".format(
            cluster=node["cluster_name"],
            inventory_hostname=node['vars']['inventory_hostname']
        )
        output = json.loads(host.check_output(cmd))
        assert status['osdmap']['osdmap']['num_osds'] == status['osdmap']['osdmap']['num_up_osds']