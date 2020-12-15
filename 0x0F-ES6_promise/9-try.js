export default function guardrail(mathFunction) {
  const queue = [];
  let val;
  try {
    val = mathFunction();
  } catch (err) {
    val = `${err.name}: ${err.message}`;
  }
  queue.push(val);
  queue.push('Guardrail was processed');
  return queue;
}
