# 🗿🔠 Rosetta Stone Paradigm for Learning C Language 🔠🗿
---


![C Language Logo](https://upload.wikimedia.org/wikipedia/commons/1/18/C_Programming_Language.svg)  
![JSON Logo](https://upload.wikimedia.org/wikipedia/commons/c/c9/JSON_vector_logo.svg)  
![XML Logo](https://upload.wikimedia.org/wikipedia/commons/c/cf/XML_logo.svg)  
![ASCII Art](https://upload.wikimedia.org/wikipedia/commons/1/1d/ASCII_Art.png)  
![Wireshark Logo](https://upload.wikimedia.org/wikipedia/commons/e/e9/Wireshark_Logo.svg)

Welcome to the **Rosetta Stone Paradigm**, a collaborative open-source project that aims to make learning the C language easier by drawing analogies to how different formats represent the same data. Inspired by the way the **Rosetta Stone** helped translate between ancient languages, this project uses multiple file formats from Wireshark dissections to teach and compare syntax across different systems.

## 🛠️ Project Overview
---

This repository focuses on taking **packet dissections** exported from Wireshark in **five different formats** and comparing them to help users learn how similar data can be represented differently in various formats, including **JSON**, **XML**, **plain text**, and more. The final output is a table of comparisons, showing how each format conveys the same meaning with different syntax.

By seeing these comparisons, you’ll gain insight into:
- **Syntax differences** between formats
- **Structure** and hierarchy of data representation
- **How different languages (like C) handle data**

## 🔍 Use Case
---

Are you learning C and curious about how different formats handle data? This tool will help by showing side-by-side comparisons of packet data, giving you a "Rosetta Stone" for understanding the syntax of C through analogy!

## ✨ Key Features
---

- **Input:** Take five different formats of Wireshark packet dissections (e.g., JSON, XML, plain text).
- **Processing:** Use an AI agent (LLM) to compare the formats and highlight differences and similarities.
- **Output:** Generate a **comparison table** showing how the same data is represented across the formats.
- **Collaborative:** Open to the community for adding more "Rosetta Stone" scenarios across various data formats and programming languages.

## 📄 Example
---

Here’s an example of what the output might look like:

| **Field Name**     | **JSON**                | **XML**                           | **Plain Text**               | **pcapng**  | **ASCII**  |
|--------------------|-------------------------|-----------------------------------|------------------------------|-------------|------------|
| Source IP          | "src_ip": "192.168.0.1"  | `<SourceIP>192.168.0.1</SourceIP>`| Source IP: 192.168.0.1       | N/A         | 192.168.0.1 |
| Destination IP     | "dst_ip": "192.168.0.2"  | `<DestinationIP>192.168.0.2</DestinationIP>`| Destination IP: 192.168.0.2   | N/A         | 192.168.0.2 |
| Protocol           | "protocol": "TCP"        | `<Protocol>TCP</Protocol>`        | Protocol: TCP                | N/A         | TCP        |
| ...                | ...                     | ...                               | ...                          | ...         | ...        |

## 🎯 Contribution Guidelines
---

We welcome contributions to this project! If you'd like to add additional scenarios or formats, feel free to:

1. Fork the repository
2. Create a new branch (`feature-your-scenario`)
3. Add your file format comparison, ensuring it's well-documented
4. Open a Pull Request (PR) with details on your addition

This project is built to grow with community contributions, so be creative and help others learn!

## 🚀 Getting Started
---

1. **Clone the repository**:
   ```bash
   git clone https://github.com/rdavidson1911/rosetta-stone-paradigm.git
   ```
2. **Install necessary dependencies** (e.g., LLM or AI tools, Python libraries):
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the tool** and load your packet dissection files in different formats:
   ```bash
   python rosetta_stone.py
   ```

## 📚 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

![Rosetta Stone Image](https://upload.wikimedia.org/wikipedia/commons/6/6d/Rosetta_Stone.JPG)

> Like the original Rosetta Stone, this project aims to help you translate across different "languages" of data formats to better understand how they work.

Join us on this journey of making C language learning easier through analogy and community!

---

# Rosetta Stone Paradigm

This project includes tools for analyzing network packet data and visualizing software dependencies.

## Apt Dependency Visualizer

The `apt_dependency_visualizer.py` script creates a visual representation of package dependencies using the apt package manager.

### Setup

1. Ensure you have Python 3 installed.
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Make sure you have Graphviz installed on your system:
   ```
   sudo apt-get install graphviz
   ```

### Usage

Run the script:
```
python apt_dependency_visualizer.py
```

You will be prompted to enter a package name and the depth of dependencies to visualize. The script will then generate a PNG image of the dependency graph.

## Contributor Philosophy

At Rosetta Stone Paradigm, we believe in understanding the deep roots of computing and language. Contributors are encouraged to engage in interdisciplinary discussions that may include:

- Chomsky's theories on language and their parallels in programming
- Information theory and its impact on data representation
- Historical developments in communication technology
- Philosophical implications of different data formats

New contributors are invited to join our regular "Deep Dive" sessions where we explore these topics and their relevance to our project goals.

Check out our [Contributor's Philosophy](docs/CONTRIBUTOR_PHILOSOPHY.md) document for more details.

## Community Discussions

We encourage all contributors and interested parties to participate in our GitHub Discussions. This is a space for:

- Sharing ideas and insights
- Asking questions and providing answers
- Exploring interdisciplinary connections
- Proposing new features or improvements

