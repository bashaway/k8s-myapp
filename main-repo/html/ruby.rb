#!/usr/bin/env ruby

puts "Content-type: text/html\n\n"
puts "<html><body>"
puts "Hello Ruby Script!<br>"

puts "<hr>\n"
puts "<pre>"
ENV.sort.each { |k,v|
    print "[\"#{k}\"] => #{v}\n" if k.start_with?("HTTP_")
}

puts "\n"

ENV.sort.each { |k,v|
    print "[\"#{k}\"] => #{v}\n" if !k.start_with?("HTTP_")
}

puts "</pre>"
puts "</body></html>"
