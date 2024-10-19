#!/bin/bash

# Function to display the 3D-style header
display_header() {
    echo -e "\e[1;34m"
    echo "╔═══════════════════════════════════════════════════════════════╗"
    echo "║                                                               ║"
    echo "║   🗿 Rosetta Stone Paradigm - Packet Dissection Exporter 🗿   ║"
    echo "║                                                               ║"
    echo "╚═══════════════════════════════════════════════════════════════╝"
    echo -e "\e[0m"
}

# Function to display a stylized message
display_message() {
    echo -e "\e[1;36m📌 $1\e[0m"
}

# Function to display an error message
display_error() {
    echo -e "\e[1;31m❌ Error: $1\e[0m"
}

# Check if Wireshark is installed
if ! command -v tshark &> /dev/null; then
    display_error "Wireshark (tshark) is not installed. Please install it first."
    exit 1
fi

# Create the rstone directory if it doesn't exist
mkdir -p rstone

# Display the header
display_header

# Prompt for the input pcap file
read -p "Enter the path to your pcap file: " pcap_file

if [ ! -f "$pcap_file" ]; then
    display_error "The specified pcap file does not exist."
    exit 1
fi

# Export formats
formats=("json" "pdml" "psml" "ek" "text")
format_names=("JSON" "PDML (XML)" "PSML (XML)" "EK (Elastic Search)" "Plain Text")

for i in "${!formats[@]}"; do
    format="${formats[$i]}"
    name="${format_names[$i]}"
    output_file="rstone/dissection_${format}.${format}"
    
    display_message "Exporting to ${name} format..."
    tshark -r "$pcap_file" -T "$format" > "$output_file"
    
    if [ $? -eq 0 ]; then
        echo -e "\e[1;32m✅ Successfully exported to $output_file\e[0m"
    else
        display_error "Failed to export to ${name} format."
    fi
done

display_message "All exports completed. Files are saved in the 'rstone' directory."
