process.stdout.write('Welcome to Holberton School, what is your name?\n');
process.stdin.on('readable', () => {
  const name = process.stdin.read();
  if (name) console.log(`Your name is: ${name}`);
});

if (process.stdout.isTTY) {
  process.stdin.on('end', () => {
    process.stdout.write('This important software is now closing\n');
  });
}
