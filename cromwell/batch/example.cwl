cwlVersion: v1.0
class: CommandLineTool
baseCommand: echo
stdout: output.txt
requirements:
  - class: DockerRequirement
    dockerPull: "ubuntu:latest"
inputs:
  message:
    type: string
    inputBinding:
      position: 1
outputs:
  output:
    type: stdout
