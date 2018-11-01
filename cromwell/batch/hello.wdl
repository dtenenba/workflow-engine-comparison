task hello {
  String addressee
  command {
    echo "Hello ${addressee}! Welcome to Cromwell . . . on AWS!"
  }
  output {
    String message = read_string(stdout())
  }
  runtime {
    docker: "centos:latest"
  }
}

workflow wf_hello {
  call hello

  output {
     hello.message
  }
}

