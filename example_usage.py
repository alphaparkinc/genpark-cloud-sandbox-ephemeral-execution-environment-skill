from client import CloudSandboxEphemeralExecutionEnvironmentClient

def main():
    client = CloudSandboxEphemeralExecutionEnvironmentClient()
    res = client.spawn_ephemeral_dev_sandbox('NODEJS_22_REACT', 8, 32)
    print('Sandbox Container: ' + res['sandbox_container_id'] + ' (Boot: ' + str(res['container_boot_latency_ms']) + 'ms)')
    print('Specs: ' + str(res['allocated_vcpus']) + ' vCPUs / ' + str(res['allocated_ram_gb']) + ' GB RAM')
    print('Tunnel: ' + res['public_https_preview_tunnel'] + ' (Isolated: ' + str(res['secure_gvisor_sandboxing_isolated']) + ')')

if __name__ == '__main__':
    main()
