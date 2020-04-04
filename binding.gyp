{
  "targets": [
    {
      "target_name": "vibrancy-wrapper",
      "sources": [
        "src/main.cc"
      ],
      "cflags": [
        "-O3"
      ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")"
      ],
      "defines": [
        "NAPI_DISABLE_CPP_EXCEPTIONS"
      ]
    }
  ]
}