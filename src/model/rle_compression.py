class RLECompression:
    def compress(self, data: str) -> str:
        """Comprime una cadena usando el método Run-Length Encoding."""
        if not data:
            return ""
        
        compressed = []
        count = 1

        for i in range(1, len(data)):
            if data[i] == data[i - 1]:
                count += 1
            else:
                compressed.append(f"{count}{data[i - 1]}")
                count = 1

        compressed.append(f"{count}{data[-1]}")
        return ''.join(compressed)
