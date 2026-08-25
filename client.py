class CloudSandboxEphemeralExecutionEnvironmentClient:
    def spawn_ephemeral_dev_sandbox(self, runtime_language='PYTHON_3_13', cpu_cores=4, memory_gb=16):
        return {
            'sandbox_container_id': 'rpl_box_8812',
            'runtime_environment': runtime_language,
            'allocated_vcpus': cpu_cores,
            'allocated_ram_gb': memory_gb,
            'container_boot_latency_ms': 280,
            'public_https_preview_tunnel': 'https://sandbox-preview.genpark.ai/app/8812',
            'collaborative_lsp_server_ready': True,
            'secure_gvisor_sandboxing_isolated': True
        }
