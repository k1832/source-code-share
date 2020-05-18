require "open3"
strongest_s = ""
longest_duration = 0
for i in 1..10 do
  input_s = (1..99).to_a.shuffle.join
  start_time = Time.now
  o, e, s = Open3.capture3("python3 extract-numbers2.py", :stdin_data=>input_s)
  duration = Time.now - start_time
  if duration > longest_duration then
    longest_duration = duration
    strongest_s = input_s
  end
end

p longest_duration, strongest_s